(function($) {
    const $results = $('#results')
    $('#submit').on('click', function (e) {
        e.preventDefault()
        let query = $('#query').val().replace(/\n/g, ' ').trim()
        if (!query.includes('LIMIT') || !query.includes('limit')) {
            query += ' LIMIT 100'
        }
        if (!query) {
            alert('Please enter a query')
            return
        }
        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000/sparql/',
            data: JSON.stringify({ query }),
            success: function (res) {
                if (res.length) {
                    $results.html(`
                        <h3 class="text-center mx-auto pb-2">
                            Query returned ${res.length - 1} result${res.length - 1 ? 's' : ''}
                        </h3>
                    `)
                    appendResults(res)
                } else {
                    $results.html(`
                        <h3 class="text-center mx-auto pb-2">
                            Query returned ${res.length} result${res.length ? 's' : ''}
                        </h3>
                    `)
                }
            },
            error: function (error) {
                console.error(error)
            }
        })
    })

    const appendResults = (res) => {
        $results.append(`
            <table class="table">
                <thead id="thead">
                </thead>
                <tbody id="tbody">
                </tbody>
            </table>
        `)
        const $tbody = $(document).find('tbody')
        res.forEach(row => {
            $tbody.append(`<tr>`)
            row.forEach(val => {
                $tbody.append(`
                    <td> ${val} </td>
                `)
            })
            $tbody.append(`</tr>`)
        })
    }
})(jQuery)