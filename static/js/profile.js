const btnsEditar = document.querySelectorAll(".edit");
const inputsForms = document.querySelectorAll(".input_formulario");
const dataAgency = document.querySelectorAll(".data_agencia");
const btnsDubmits = document.querySelectorAll(".btnSubmit")


btnsEditar.forEach((btnEditar) => {
  btnEditar.addEventListener("click", () => {

    inputsForms.forEach((input) => {
      if (input.classList.contains("hidden")) {
        input.classList.remove("hidden");
      } else {
        input.classList.add("hidden");
      }
    });

    dataAgency.forEach((data) => {
      if (data.classList.contains("hidden")) {
        data.classList.remove("hidden");
      } else {
        data.classList.add("hidden");
      }
    });

    btnsDubmits.forEach(btn=>{
        if (btn.classList.contains("hidden")) {
            btn.classList.remove("hidden");
          } else {
            btn.classList.add("hidden");
          }
    });

  });
});
