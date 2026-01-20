document.getElementById("studentForm").addEventListener("submit", function(e) {
    e.preventDefault();

    let formData = new FormData(this);

    fetch("/submit", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("response").innerText =
            data.message + " | Name: " + data.name + " | Age: " + data.age;
    });
});
