(function($) {
    const $results = $('#results')
    $('#submit').on('click', function (e) {
        e.preventDefault()
        const query = $('#query').val().replace(/\n/g, ' ').trim()
        if (!query) {
            alert('Please enter a query')
            return
        }
        $.ajaxSetup({
            headers: {
                'accept': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        })
        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000/sparql/',
            data: JSON.stringify({ query }),
            success: function (res) {
                $results.html(`
                    <h3 class="text-center mx-auto pb-2">
                        Query returned ${res.length} result${res.length ? 's' : ''}
                    </h3>
                `)
                if (res.length) {
                    appendResults(res)
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