document.querySelectorAll('.save').forEach(saveBtn => {
    saveBtn.addEventListener('click', async (e) => {
        const v_id = e.target.getAttribute('for')
        await fetch('api/save', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ v_id })
        })

        document.location.reload()
    })
})

document.querySelectorAll('.unsave').forEach(unsaveBtn => {
    unsaveBtn.addEventListener('click', async (e) => {
        const v_id = e.target.getAttribute('for')
        await fetch('api/unsave', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ v_id })
        })

        document.location.reload()
    })
})

document.querySelectorAll('.delete-book').forEach(delBtn => {
    delBtn.addEventListener('click', async (e) => {
        const v_id = e.target.getAttribute('for')
        await fetch('api/delete', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ v_id })
        })

        document.location.reload()
    })
})

