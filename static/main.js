console.log("hello")
// This function will reload the page every 5 seconds (5000 milliseconds)
function autoReload() {
    setTimeout(function() {
        location.reload();
    }, 5000);
}