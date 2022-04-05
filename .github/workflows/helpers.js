const https = require('https')

function sortVersions(versions) {
    return versions.map(
        a => a.replace(/\d+/g, n => +n + 100000)
    ).sort().map(
        a => a.replace(/\d+/g, n => +n - 100000)
    )
}

async function getDownloadURL(packageName, version) {
    const options = {
        hostname: 'pypi.org',
        port: 443,
        path: `/pypi/${packageName}/json`,
        method: 'GET'
    }

    return new Promise((resolve, reject) => {
        const req = https.request(options, res => {
            if (res.statusCode < 200 || res.statusCode >= 300) {
                return reject(new Error(`Status Code: ${res.statusCode}`))
            }
            const data = []
            res.on("data", chunk => data.push(chunk))
            res.on("end", () => {
                const response = JSON.parse(Buffer.concat(data).toString())
                console.log('getDownloadURL response', response)
                const versionsData = response.releases[version]
                console.log('getDownloadURL versionsData', versionsData)
                if (!versionsData) {
                    return reject(new Error(`No download URLs found for ${packageName} ${version}`))
                }

                const versionData = versionsData.find(x => x.packagetype === 'bdist_wheel') || versionsData[0]
                console.log('getDownloadURL result', versionData.url)
                resolve(versionData.url)
            })
        })
        req.on("error", reject)
        req.end()
    })
}

async function getReleaseVersions(packageName) {
    const options = {
        hostname: 'pypi.org',
        port: 443,
        path: `/pypi/${packageName}/json`,
        method: 'GET'
    }

    return new Promise((resolve, reject) => {
        const req = https.request(options, res => {
            if (res.statusCode < 200 || res.statusCode >= 300) {
                return reject(new Error(`Status Code: ${res.statusCode}`))
            }
            const data = []
            res.on("data", chunk => data.push(chunk))
            res.on("end", () => {
                const response = JSON.parse(Buffer.concat(data).toString())
                resolve(Object.keys(response.releases))
            })
        })
        req.on("error", reject)
        req.end()
    })
}

function getNextPostVersion(version) {
    if (version.includes('post')) {
        const post = version.match(/\d+$/)[0]
        const newPost = `${parseInt(post) + 1}`
        return version.replace(/\d+$/, newPost)
    }
    return `${version}.post1`
}

async function getBoto3Version() {
    const versions = await getReleaseVersions('boto3')
    return sortVersions(versions).pop()
}

async function getAioBotocoreVersion() {
    const versions = await getReleaseVersions('aiobotocore')
    return sortVersions(versions).pop()
}

async function getTypesAioBotocoreVersions(aiobotocoreVersion) {
    const allVersions = await getReleaseVersions('types-aiobotocore')
    const versions = allVersions.filter(v => v === aiobotocoreVersion || v.startsWith(`${aiobotocoreVersion}.`))
    return sortVersions(versions)
}

async function getStubsVersions(boto3Version) {
    const allVersions = await getReleaseVersions('boto3-stubs')
    const versions = allVersions.filter(v => v === boto3Version || v.startsWith(`${boto3Version}.`))
    return sortVersions(versions)
}

function getBotocoreVersion(version) {
    const minor = parseInt(version.match(/\d+\.(\d+)\./)[1]) + 3
    return version.replace(/\.\d+/, `.${minor}`)
}

async function extractVersions({ core, context }) {
    core.setOutput('version', '')

    const boto3Version = (
        (context.payload.inputs && context.payload.inputs.boto3_version) ?
            context.payload.inputs.boto3_version :
            await getBoto3Version()
    )
    const force = context.payload.inputs ? context.payload.inputs.force !== 'false' : false

    let buildAll = (context.payload.inputs && context.payload.inputs.build_all !== 'false') ? 'true' : 'false'
    if (boto3Version.endsWith('.0')) {
        core.info(`Boto3 version is not a micro release ${boto3Version}, building all packages`)
        buildAll = 'true'
    }

    const smartVersion = context.payload.inputs ? context.payload.inputs.smart_version !== 'false' : false
    core.info(`Smart version = ${smartVersion}`)
    core.setOutput('no_smart_version', smartVersion ? '' : '--no-smart-version --skip-published')

    const botocoreVersion = getBotocoreVersion(boto3Version)
    core.info(`Boto3 version = ${boto3Version}`)
    core.setOutput('boto3-version', boto3Version)

    core.info(`Botocore version = ${botocoreVersion}`)
    core.setOutput('botocore-version', botocoreVersion)

    core.info(`Build all packages = ${buildAll}`)
    core.setOutput('build-all', buildAll)

    const versions = await getStubsVersions(boto3Version)
    core.info(`Built versions ${versions}`)

    if (context.payload.inputs && context.payload.inputs.stubs_version) {
        const buildVersion = context.payload.inputs.stubs_version
        core.info(`Forced boto3-stubs version: ${buildVersion}`)
        core.info(`Build version = ${buildVersion}`)
        core.setOutput('version', buildVersion)
        return
    }

    if (versions.length && !force) {
        core.info('Builds found, skipping')
        return
    }

    if (!versions.length) {
        core.info(`No builds found, building initial ${boto3Version}`)
        core.setOutput('version', boto3Version)
        return
    }

    const lastBuildVersion = versions.pop()
    core.info(`Last build version ${lastBuildVersion}`)

    const buildVersion = getNextPostVersion(lastBuildVersion)
    core.info(`Build version = ${buildVersion}`)
    core.setOutput('version', buildVersion)
}

async function extractDownloadLinks({ core }) {
    const boto3URL = await getDownloadURL('boto3', process.env.BOTO3_VERSION)
    core.info(`Boto3 download URL: ${boto3URL}`)
    core.setOutput('boto3-url', boto3URL)

    const botocoreURL = await getDownloadURL('botocore', process.env.BOTOCORE_VERSION)
    core.info(`Botocore download URL: ${botocoreURL}`)
    core.setOutput('botocore-url', botocoreURL)
}


async function extractAioBotocoreVersions({ core, context }) {
    core.setOutput('version', '')

    const aiobotocoreVersion = (
        (context.payload.inputs && context.payload.inputs.aiobotocore_version) ?
            context.payload.inputs.aiobotocore_version :
            await getAioBotocoreVersion()
    )

    core.info(`Aiobotocore version = ${aiobotocoreVersion}`)
    core.setOutput('aiobotocore-version', aiobotocoreVersion)

    const force = context.payload.inputs ? context.payload.inputs.force !== 'false' : false

    let buildAll = (context.payload.inputs && context.payload.inputs.build_all !== 'false') ? 'true' : 'false'
    if (aiobotocoreVersion.endsWith('.0')) {
        core.info(`Aiobotocore version is not a micro release ${aiobotocoreVersion}, building all packages`)
        buildAll = 'true'
    }

    const smartVersion = context.payload.inputs ? context.payload.inputs.smart_version !== 'false' : false
    core.info(`Smart version = ${smartVersion}`)
    core.setOutput('no_smart_version', smartVersion ? '' : '--no-smart-version --skip-published')

    core.info(`Build all packages = ${buildAll}`)
    core.setOutput('build-all', buildAll)

    const versions = await getTypesAioBotocoreVersions(aiobotocoreVersion)
    core.info(`Built versions ${versions}`)

    if (context.payload.inputs && context.payload.inputs.stubs_version) {
        const buildVersion = context.payload.inputs.stubs_version
        core.info(`Forced types-aiobotocore version: ${buildVersion}`)
        core.info(`Build version = ${buildVersion}`)
        core.setOutput('version', buildVersion)
        return
    }

    if (versions.length && !force) {
        core.info('Builds found, skipping')
        return
    }

    if (!versions.length) {
        core.info(`No builds found, building initial ${aiobotocoreVersion}`)
        core.setOutput('version', aiobotocoreVersion)
        return
    }

    const lastBuildVersion = versions.pop()
    core.info(`Last build version ${lastBuildVersion}`)

    const buildVersion = getNextPostVersion(lastBuildVersion)
    core.info(`Build version = ${buildVersion}`)
    core.setOutput('version', buildVersion)
}

async function extractAioBotocoreDownloadLinks({ core }) {
    const aiobotocoreURL = await getDownloadURL('aiobotocore', process.env.AIOBOTOCORE_VERSION)
    core.info(`aiobotocore download URL: ${aiobotocoreURL}`)
    core.setOutput('aiobotocore-url', aiobotocoreURL)
}

async function extractVersionsFromInput({ core, context }) {
    const inputBoto3Version = context.payload.inputs && context.payload.inputs.boto3_version
    const boto3Version = inputBoto3Version ? inputBoto3Version : await getBoto3Version()
    const botocoreVersion = getBotocoreVersion(boto3Version)
    core.info(`Boto3 version ${boto3Version}`)
    core.info(`Botocore version ${botocoreVersion}`)
    core.setOutput('version', boto3Version)
    core.setOutput('boto3-version', boto3Version)
    core.setOutput('botocore-version', botocoreVersion)
}

module.exports = {
    getDownloadURL,
    sortVersions,
    getNextPostVersion,
    getReleaseVersions,
    getBoto3Version,
    getStubsVersions,
    getBotocoreVersion,
    extractVersions,
    extractDownloadLinks,
    extractAioBotocoreVersions,
    getAioBotocoreVersion,
    getTypesAioBotocoreVersions,
    extractAioBotocoreDownloadLinks,
    extractVersionsFromInput,
}
