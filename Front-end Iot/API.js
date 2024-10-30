const serverUrl = 'http://192.168.100.141:5000';  
    
        document.getElementById('stop-btn').addEventListener('click', function() {
            fetch(`${serverUrl}/stop_capture`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ command: 'stop' })
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                alert('Captura parada!');  
            })
            .catch(error => console.error('Erro ao parar a captura:', error));
        });
    
        document.getElementById('start-btn').addEventListener('click', function() {
            fetch(`${serverUrl}/stop_capture`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ command: 'start' })
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                alert('Captura iniciada!');  
            })
            .catch(error => console.error('Erro ao iniciar a captura:', error));
        });