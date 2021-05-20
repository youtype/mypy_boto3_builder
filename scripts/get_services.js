// https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html
(() => {
    const els = [...document.querySelectorAll('.document .toctree-l1 > .reference[href]')]
    els.sort((a, b) => a.href.localeCompare(b.href))
    const lines = els.map(el => `        ServiceName("${el.getAttribute('href').split(".")[0]}", "${el.innerText}"),`)
    console.log(lines.join('\n'))
})()
