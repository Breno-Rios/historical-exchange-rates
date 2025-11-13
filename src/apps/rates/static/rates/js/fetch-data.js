
document.addEventListener('DOMContentLoaded', () => {
    
    const form = document.getElementById('rates-form')

    form.addEventListener('submit', async function(event){
        event.preventDefault();

        const startDate = form.querySelector('[name="start_date"]').value;
        const endDate = form.querySelector('[name="end_date"]').value;
        const currencyCode = form.querySelector('[name="currency"]').value;
        
        await new Promise(resolve => setTimeout(resolve, 10))
        
        const url = `/dashboard/${startDate}/${endDate}/?currency=${currencyCode}`;
        
        try{
            showLoading();
            const response = await fetch(url);
            const jsonData = await response.json()
            if(response.ok){
                hideMessage()
                updateChart(jsonData)
            }else{
                showMessage(jsonData.error, 'danger')
            }
            hideLoading();
        }catch (e){
            console.log('Error to request:', e)
            showMessage(`Error to request {response.status}`, 'danger')
            hideLoading()
        }finally{
             hideLoading();

        }

    })


    function updateChart(data) {
        if (!data || !data.length) {
            console.warn("No data received to update chart");
            return;
        }
        
        const categories = data.map(d => d.date);
        const values = data.map(d => parseFloat(d.value) || 0);
        const currencyStr = data.map(d => d.currency)
        
        window.chart.xAxis[0].setCategories(categories);
        window.chart.series[0].setData(values);

        chart.update({
            tooltip: {
                pointFormat: `{point.y} ${currencyStr[0]}`
            }
        });
    }

})