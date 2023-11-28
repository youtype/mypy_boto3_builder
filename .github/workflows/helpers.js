let fetch = null;
let core = null;
let context = null;

function setupGlobals(globals) {
    fetch = globals.fetch
    if (!fetch) throw new Error('fetch is not defined')

    core = globals.core
    if (!core) throw new Error('core is not defined')

    context = globals.context
    if (!context) throw new Error('context is not defined')
}

function sortVersions(versions) {
    return versions.map(
        a => a.replace(/\d+/g, n => `${parseInt(n) + 100000}`)
    ).sort().map(
        a => a.replace(/\d+/g, n => `${parseInt(n) - 100000}`)
    )
}

async function getDownloadURL(packageName, version) {
    if (!packageName) throw new Error('packageName is not defined')
    if (!version) throw new Error(`version is not defined for ${packageName}`)
    const response = await fetch(`https://pypi.org/pypi/${packageName}/json`)
    const data = await response.json()
    const versionsData = data.releases[version]
    if (!versionsData) {
        throw new Error(`No download URLs found for ${packageName} ${version}`)
    }
    const versionData = versionsData.find(x => x.packagetype === 'bdist_wheel') || versionsData[0]
    core.debug('getDownloadURL result', versionData.url)
    return versionData.url
}

async function getReleaseVersions(packageName) {
    if (!packageName) throw new Error('packageName is not defined')
    const response = await fetch(`https://pypi.org/pypi/${packageName}/json`)
    const data = await response.json()
    return Object.keys(data.releases)
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

async function getAioBoto3Version() {
    const versions = await getReleaseVersions('aioboto3')
    return sortVersions(versions).pop()
}

async function getTypesAioBotocoreVersions(aiobotocoreVersion) {
    const allVersions = await getReleaseVersions('types-aiobotocore')
    const versions = allVersions.filter(v => v === aiobotocoreVersion || v.startsWith(`${aiobotocoreVersion}.`))
    return sortVersions(versions)
}

async function getTypesAioBoto3Versions(aioboto3Version) {
    const allVersions = await getReleaseVersions('types-aioboto3')
    const versions = allVersions.filter(v => v === aioboto3Version || v.startsWith(`${aioboto3Version}.`))
    return sortVersions(versions)
}

async function getStubsVersions(boto3Version) {
    const allVersions = await getReleaseVersions('boto3-stubs')
    const versions = allVersions.filter(v => v === boto3Version || v.startsWith(`${boto3Version}.`))
    return sortVersions(versions)
}

function getBotocoreVersion(version) {
    return version
}

async function extractVersions() {
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

    const extraFlags = []

    const skipPublished = context.payload.inputs ? context.payload.inputs.skip_published !== 'false' : true
    const noSmartVersion = context.payload.inputs ? context.payload.inputs.no_smart_version !== 'false' : true
    if (skipPublished) extraFlags.push('--skip-published')
    if (noSmartVersion) extraFlags.push('--no-smart-version')

    core.info(`Extra flags = ${extraFlags}`)
    core.setOutput('extra-flags', extraFlags.join(' '))

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

async function extractDownloadLinks() {
    const boto3URL = await getDownloadURL('boto3', process.env.BOTO3_VERSION)
    core.info(`Boto3 download URL: ${boto3URL}`)
    core.setOutput('boto3-url', boto3URL)

    const botocoreURL = await getDownloadURL('botocore', process.env.BOTOCORE_VERSION)
    core.info(`Botocore download URL: ${botocoreURL}`)
    core.setOutput('botocore-url', botocoreURL)
}


async function extractAioBotocoreVersions() {
    core.setOutput('version', '')

    const aiobotocoreVersion = (
        (context.payload.inputs && context.payload.inputs.aiobotocore_version) ?
            context.payload.inputs.aiobotocore_version :
            await getAioBotocoreVersion()
    )

    core.info(`Aiobotocore version = ${aiobotocoreVersion}`)
    core.setOutput('aiobotocore-version', aiobotocoreVersion)

    const force = context.payload.inputs ? context.payload.inputs.force !== 'false' : false

    const extraFlags = []

    const skipPublished = context.payload.inputs ? context.payload.inputs.skip_published !== 'false' : false
    const noSmartVersion = context.payload.inputs ? context.payload.inputs.no_smart_version !== 'false' : true
    if (skipPublished) extraFlags.push('--skip-published')
    if (noSmartVersion) extraFlags.push('--no-smart-version')

    core.info(`Extra flags = ${extraFlags}`)
    core.setOutput('extra-flags', extraFlags.join(' '))

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

async function extractAioBoto3Versions() {
    core.setOutput('version', '')

    const aioboto3Version = (
        (context.payload.inputs && context.payload.inputs.aioboto3_version) ?
            context.payload.inputs.aioboto3_version :
            await getAioBoto3Version()
    )

    core.info(`Aioboto3 version = ${aioboto3Version}`)
    core.setOutput('aioboto3-version', aioboto3Version)

    const force = context.payload.inputs ? context.payload.inputs.force !== 'false' : false

    const versions = await getTypesAioBoto3Versions(aioboto3Version)
    core.info(`Built versions ${versions}`)

    if (context.payload.inputs && context.payload.inputs.stubs_version) {
        const buildVersion = context.payload.inputs.stubs_version
        core.info(`Forced types-aioboto3 version: ${buildVersion}`)
        core.info(`Build version = ${buildVersion}`)
        core.setOutput('version', buildVersion)
        return
    }

    if (versions.length && !force) {
        core.info('Builds found, skipping')
        return
    }

    if (!versions.length) {
        core.info(`No builds found, building initial ${aioboto3Version}`)
        core.setOutput('version', aioboto3Version)
        return
    }

    const lastBuildVersion = versions.pop()
    core.info(`Last build version ${lastBuildVersion}`)

    const buildVersion = getNextPostVersion(lastBuildVersion)
    core.info(`Build version = ${buildVersion}`)
    core.setOutput('version', buildVersion)
}

async function extractAioBotocoreDownloadLinks() {
    const aiobotocoreURL = await getDownloadURL('aiobotocore', process.env.AIOBOTOCORE_VERSION)
    core.info(`aiobotocore download URL: ${aiobotocoreURL}`)
    core.setOutput('aiobotocore-url', aiobotocoreURL)
}

async function extractAioBoto3DownloadLinks() {
    const aioboto3URL = await getDownloadURL('aioboto3', process.env.AIOBOTO3_VERSION)
    core.info(`aioboto3 download URL: ${aioboto3URL}`)
    core.setOutput('aioboto3-url', aioboto3URL)
}

async function extractVersionsFromInput() {
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
    setupGlobals,
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
    extractAioBoto3Versions,
    extractAioBoto3DownloadLinks,
}
