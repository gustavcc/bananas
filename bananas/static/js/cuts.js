const search_btn = document.querySelector('#search-btn')
const search = document.querySelector('#search')
const id_input = document.querySelector('#id')

let id = id_input.value;

search_btn.addEventListener('click',()=>{        
    window.location.href = `http://127.0.0.1:8000/lot/${id}?search=${search.value}`;
})

// const dialogView = document.getElementById('ver-preco')

// function viewPrice(cut){
//     var id = cut.id
//     const priceValue = document.querySelector('#price-value')

//     var valorCurrent = priceValue.textContent

//     console.log(valorCurrent);
    

//     var novoValor = valorCurrent.replace('{cuts.ID.preco_total}', `{cuts.${id}.preco_total}`)

//     console.log(novoValor);
    

//     priceValue.textContent = novoValor
//     dialogView.showModal();
   
//     console.log(`cuts.0.preco_total`)
           
// }

// document.getElementById('dialog-sair2').addEventListener('click', ()=>{
//     dialogView.close();
// })