const config = {};
window.ClassicEditor
    .create(document.querySelector('#editor'), config)
    .catch(error => {
        console.error(error);
    });
}
