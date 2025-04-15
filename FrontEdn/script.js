
document.addEventListener("DOMContentLoaded",() =>{
    fetchProdutos();

})

function fetchProdutos (){
    fetch("http://localhost:8000/api/produtos/")
    .then(res => res.jason)
    .then(data => renderProdutos(data))
    .catch(err=> console.error ("Erro ao buscar produtos", err));
}

function renderProdutos(produtos){

    const container = document.getElementById("produtos-container");
    container.innerHTML ="";

    produtos.forEach(produtos => {
    const card = document.createElement("div");
    card.className = "produto";
    card.innerHTML = `
        <h2>${produtos.nome}</h2>
        <p>${produtos.descricao}</p>
        <p class="preco"> R$ ${produtos.preco}</p>
        <p> <strong>Categoria:<strong> ${produtos.categoria.nome}</p>
    `;
    conatainer.appendChild(card);
    });

    
}