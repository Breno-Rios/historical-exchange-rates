// 1. Global config deve vir antes
Highcharts.setOptions({
    chart: {
        style: {
            fontFamily: 'Roboto, sans-serif',
            fontSize: '16px'
        }
    },
    title: {
        style: {
            fontSize: '22px'
        }
    },
    xAxis: {
        labels: {
            style: {
                fontSize: '14px'
            }
        },
        title: {
            style: {
                fontSize: '16px'
            }
        }
    },
    yAxis: {
        labels: {
            style: {
                fontSize: '14px'
            }
        },
        title: {
            style: {
                fontSize: '16px'
            }
        }
    },
    legend: {
        itemStyle: {
            fontSize: '14px'
        }
    },
    tooltip: {
        style: {
            fontSize: '14px'
        }
    }
});

document.addEventListener('DOMContentLoaded', function () {
  const categories = JSON.parse(
    document.getElementById('chart-categories').textContent
  );
  const values = JSON.parse(
    document.getElementById('chart-values').textContent
  );
   const base = JSON.parse(
    document.getElementById('chart-base').textContent
  );
  const currency = JSON.parse(
    document.getElementById('chart-currency').textContent
  );

let value_float = null;
if (Array.isArray(values)) {
    value_float = values
      .map(Number)                        
      .map(v => Number(v.toFixed(4)));   
} 

  const firstDate  = categories[0];
  const lastDate   = categories[categories.length - 1];
  const base_str  = base[0];
  const currency_str  = currency[0];

  const titleStr = `${base_str} -> ${currency_str}: ${firstDate} to ${lastDate}`;

Highcharts.chart('container-highcharts', {
    title: {
        text: titleStr
    },

    accessibility: {
        point: {
            valueDescriptionFormat:
                '{xDescription}{separator}{value} million(s)'
        }
    },

    xAxis: {
        title: {
            text: 'Date'
        },
        categories: categories,
    },

    yAxis: {
        type: 'logarithmic',
        title: {
            text: 'Exchange Rates'
        }
    },

    tooltip: {
        headerFormat: '<b>{series.name}</b><br />',
        pointFormat: `{point.y} ${currency_str}`
    },

    series: [{
        name: 'Rates',
        data: value_float,
        color: 'var(--highcharts-color-1, #007891)'
    }]
});
});