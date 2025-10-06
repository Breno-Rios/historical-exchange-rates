
document.addEventListener('DOMContentLoaded', () => {
    
    const form = document.getElementById('rates-form')

    form.addEventListener('submit', async function(event){
        event.preventDefault();

        const startDate = form.querySelector('[name="start_date"]').value;
        const endDate = form.querySelector('[name="end_date"]').value;
        const currencyCode = form.querySelector('[name="currency"]').value;
        
        const url = `/dashboard/?start-date=${startDate}&end-date=${endDate}&currency-code=${currencyCode}`;
        
        try{
            const response = await fetch(url);
            const jsonData = await response.json()

            if(response.ok){
                hideMessage()
                updateChart(jsonData.data)
            }else{
                showMessage(jsonData.error, 'danger')
            }
            
        }catch (e){
            console.log('Error to request:', e)
            showMessage(`Error to request {response.status}`, 'danger')
        }

    })


    function updateChart(data) {
        if (!data || !data.length) {
            console.warn("No data received to update chart");
            return;
        }
        
        const categories = data.map(d => d.date);
        const values = data.map(d => parseFloat(d.value) || 0);
        const currencyStr = data.map(d => d.base_code)
        
        window.chart.xAxis[0].setCategories(categories);
        window.chart.series[0].setData(values);

        chart.update({
            tooltip: {
                pointFormat: `{point.y} ${currencyStr[0]}`
            }
        });
    }

})