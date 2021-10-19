function TransferForm(){
    var submission;
    if (confirm("Do you wish to transfer money?")) {
        location.href = "/transfer"
    } else {
        alert("okay! Have a good day!")
    }
    document.getElementById("transfer").innerHTML = submission;

}

function submitform(){
    alert("Money transaction was successful!!")
}