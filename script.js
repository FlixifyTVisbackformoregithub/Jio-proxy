document.getElementById('proxyForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const url = document.getElementById('url').value;
    fetch(`/proxy?url=${encodeURIComponent(url)}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            document.getElementById('responseContainer').innerHTML = data;
        })
        .catch(error => {
            document.getElementById('responseContainer').innerHTML = 'Error: ' + error;
        });
});
