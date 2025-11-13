const button = document.getElementById('button');
function showLoading() {

    button.disabled = true;
    button.style.backgroundColor = '#ffffff';
    button.innerHTML = '<span class="loader"></span>';
}
function hideLoading() {
    
    button.innerHTML = 'Search';
    button.disabled = false;
    button.style.backgroundColor = '#193b4f';

}