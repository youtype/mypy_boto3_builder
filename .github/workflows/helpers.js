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
                return reject(new Error(`Status Code: ${res.statusCode}`));
            }
            const data = [];
            res.on("data", chunk => data.push(chunk));
            res.on("end", () => {
                const response = JSON.parse(Buffer.concat(data).toString())
                const versionsData = response.releases[version]

                const versionData = versionsData.find(x => x.packagetype === 'bdist_wheel') || versionsData[0]
                resolve(versionData.url)
            })
        });
        req.on("error", reject)
        req.end();
    });
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
                return reject(new Error(`Status Code: ${res.statusCode}`));
            }
            const data = [];
            res.on("data", chunk => data.push(chunk));
            res.on("end", () => {
                const response = JSON.parse(Buffer.concat(data).toString())
                resolve(Object.keys(response.releases))
            })
        });
        req.on("error", reject)
        req.end();
    });
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

    const botocoreVersion = getBotocoreVersion(boto3Version)
    core.info(`Boto3 version = ${boto3Version}`)
    core.setOutput('boto3-version', boto3Version)

    core.info(`Botocore version = ${botocoreVersion}`)
    core.setOutput('botocore-version', botocoreVersion)

    core.info(`Build all packages = ${buildAll}`)
    core.setOutput('build-all', buildAll)

    const versions = await getStubsVersions(boto3Version)
    core.info(`Built versions ${versions}`)

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

module.exports = {
    sortVersions,
    getNextPostVersion,
    getReleaseVersions,
    getBoto3Version,
    getStubsVersions,
    getBotocoreVersion,
    extractVersions,
    extractDownloadLinks,
}