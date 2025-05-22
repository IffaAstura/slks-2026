document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('userForm');
    const result = document.getElementById('result');

    form.addEventListener('submit', async function (e) {
        e.preventDefault();

        const nama = document.getElementById('nama').value;
        const kelas = document.getElementById('kelas').value;
        const sekolah = document.getElementById('sekolah').value;
        const gender = document.querySelector('input[name="gender"]:checked').value;

        const data = {
            nama,
            kelas,
            sekolah,
            gender
        };

        try {
            //Replace this with your API Gateway URL
            const response = await fetch('https://xzixnwbs3i.execute-api.us-west-2.amazonaws.com/prod/app1', { 
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            const resultData = await response.json();
            result.innerText = resultData.body || 'Data berhasil dikirim.';
        } catch (error) {
            result.innerText = 'Terjadi kesalahan saat mengirim data.';
            console.error('Error:', error);
        }
    });
});
