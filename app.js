const nombre = document.getElementById("NA");
const database = firebase.database();
btn1.addEventListener("click", (e)=>{
    e.preventDefault();
    database.ref("./RegistroU").set({
        nombre:nombre.value});
});