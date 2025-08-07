

async function buildList(){
    let wrapper = document.getElementById('list-wrapper')
    wrapper.innerHTML = ''

    const url = 'http://127.0.0.1:8000/api/tasklist/'

    let api = await fetch(url)
    let resp = await api.json()
    
    console.log("Data: ", resp)

    let list = resp

    for (let i in list){
        var title = `<p id='task' class="title hover:cursor-pointer font-mono completed text-base">${list[i].title}</p>`
        if(list[i].completed == true){
            title = `<strike id='task' class="title hover:cursor-pointer font-mono completed text-gray-300 text-base">${list[i].title}</strike>`

        }
        let item = `
            <div class="flex flex-shrink-0 h-[40px] shadow ring ring-gray-300 items-center justify-between rounded-sm  border-gray-200 pl-3">
                ${title}
                <div class="flex items-center justify-between">
                    <button class="h-[70%] rounded  px-2 border hover:cursor-pointer hover:bg-green-500 hover:text-white border-green-500 text-green-600 mr-5 edit">Edit</button>
                <button class="h-[70%] rounded  px-2 border hover:cursor-pointer border-gray-400 hover:border-red-600 mr-4 delete ">-</button>
                </div>
          </div>
        `
        
        
        wrapper.innerHTML += item

        
        
    }

    for (let i in list) {
        let del = document.getElementsByClassName('delete')[i]
        let edit = document.getElementsByClassName('edit')[i]
        let title = document.getElementsByClassName('title')[i] 

        edit.addEventListener('click', (function (item) {

            return () => {
                editItem(item)
            }


        })(list[i]))
        del.addEventListener('click', (function (item) {

            return () => {
                deleteItem(item)
            }


        })(list[i]))
        title.addEventListener('click', (function (item) {

            return () => {
                strikeUnstrike(item)
            }


        })(list[i]))
    }

   

        


    
   
}



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


let activeItem = null
let form = document.getElementById('form-wrapper')
form.addEventListener('submit', (e) => {
    e.preventDefault()
    
    let url = 'http://127.0.0.1:8000/api/taskcreate/'
    if (activeItem != null) {
        url = `http://127.0.0.1:8000/api/taskupdate/${activeItem.id}`
        activeItem = null
    }


    let title = document.getElementById('title').value

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type' : 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'title' : title})

    })
    .then((resp) => buildList(),
        document.getElementById("title").value = ""
    )

})

buildList()








function editItem(item){
    console.log('item clicked', item)
    activeItem = item
    document.getElementById('title').value = activeItem.title

    

}

function deleteItem(item) {
    console.log('deleted item clicked', item)
   let url = `http://127.0.0.1:8000/api/taskdelete/${item.id}`
   fetch(url, {
       method: 'DELETE',
       headers: {
           'Content-type': 'application/json',
           'X-CSRFToken': csrftoken,
       },
    }
    
   ).then((resp) => buildList()
   )
}




function strikeUnstrike(item) {
    item.completed = !item.completed
    
    


    console.log('StrikeUnstrike', item.completed)
    let url = `http://127.0.0.1:8000/api/taskupdate/${item.id}`
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'title': item.title, 'completed': item.completed })
    }

    ).then((resp) => buildList()
    )
}


 // for (let i in list) {
    //     let comple = document.getElementsByClassName('completed')[i]
    //     let item = list[i]
    //     if (item.completed == false) {
    //         comple.style.textDecoration = 'line-through';
    //         comple.style.color = 'gray'
    //     }
              

    //     comple.addEventListener('click', () => {

    //         if (item.completed == false){
    //             item.completed = true
    //             comple.style.textDecoration = 'none';
    //             comple.style.color = 'black'
                
    //         }
    //         else{
    //             item.completed = false               
    //         }
    //     }

    //     )

        



    // }