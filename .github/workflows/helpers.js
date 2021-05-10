const https = require('https')

function sortVersions(versions) {
    return versions.map(
        a => a.replace(/\d+/g, n => +n + 100000)
    ).sort().map(
        a => a.replace(/\d+/g, n => +n - 100000)
    )
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

module.exports = {
    sortVersions,
    getNextPostVersion,
    getReleaseVersions,
    getBoto3Version,
    getStubsVersions,
    getBotocoreVersion
}