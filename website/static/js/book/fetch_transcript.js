const transcriptParentContainer = document.getElementById('transcript-parent-container')
const loading = document.getElementById('loading-screen')

async function fetchTranscript() {
    const res = await fetch(`/api/transcript?v=${v_id}`)
    const transcript = await res.json()

    let innerHTMLContent
    transcript.forEach(line => {
        if (isNaN(line.text)) {
            [ms, mews] = line.start.toString().split('.')
            innerHTMLContent += `<p start=${line.start} ms=${ms} mews=${mews || 0}><span>${line.text}</span></p>`
        }
    })

    transcriptParentContainer.innerHTML = innerHTMLContent

    loading.style.opacity = 0
    loading.style.display = 'none'
}

fetchTranscript()