function confirmDelete(uid,path) {
    bootbox.confirm("Are you sure want to delete '"+uid+"'?", function (result) {
        if (result) {
            window.location.href = path;
        }
    });
}

function editPerson(path) {
    window.location.href = path;
}



