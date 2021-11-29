(async function ($) {
    const $results = $('#results')
    const ajaxPromise = (url) => {
        return new Promise((resolve, reject) => {
            $.ajax({
                url,
                type: 'GET',
                success: function (data) {
                    resolve(data)
                },
                error: function (error) {
                    reject(error)
                },
            })
        })
    }
    const getSubjects = ajaxPromise('/subject')
    const getPredicates = ajaxPromise('/predicate')
    const getObjects = ajaxPromise('/object')
    const [subjects, predicates, objects] = await Promise.all([getSubjects, getPredicates, getObjects])

    appendSelect = (divId, data) => {
        $(`#${divId}`).append(`
            <option value="${data}">${data}</option>
        `)
    }

    subjects.forEach(data => appendSelect('subject', data))
    predicates.forEach(data => appendSelect('predicate', data))
    objects.forEach(data => appendSelect('object', data))

    $('#submit').on('click', function (e) {
        e.preventDefault()
        let data = {
            subject: $('#subject').val(),
            predicate: $('#predicate').val(),
            object: $('#object').val(),
        }
        const isNull = Object.entries(data).every(([key, value]) => value === '')
        const allThree = Object.entries(data).every(([key, value]) => value !== '')
        if (isNull) {
            alert('Please enter a query')
            return
        } else if (allThree) {
            alert('You can only choose 2 options')
            return
        }
        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:8000/query/',
            data: JSON.stringify(data),
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
    })
})(jQuery)