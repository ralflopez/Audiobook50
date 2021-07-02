document.querySelectorAll('.save').forEach(saveBtn => {
    saveBtn.addEventListener('click', async (e) => {
        const v_id = e.target.getAttribute('for')
        const res = await fetch('api/save', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ v_id })
        })
        const data = await res.json()

        console.log(data)
    })
})