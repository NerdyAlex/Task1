
let wrapper = document.getElementById("wrapper");

let PinView = document.getElementById("PinView");


if (wrapper){

    

    async function list() {
        wrapper.innerHTML = ""
        
        

        let url = "http://127.0.0.1:8000/api/list/";
        let response = await fetch(url)
        let data = await response.json()
        console.log(data)
        
        
       

        for (let i in data) {
            let info = data[i]
            
            let item = `
            
                    <div class="edit view relative  break-inside-avoid mb-5 w-[180px]">
                    <img class="rounded-2xl w-full h-auto" src=${info.img_url}/>
                    <p>${info.title}</p>
                    <div class="flex justify-between items-center">
                        <small class="font-bold">${info.author}</small>
                        <button  class="btn  hover:cursor-pointer hover:bg-pink-700 flex items-center justify-center  w-6 h-6 rounded-full bg-pink-400">
                            <img class="w-[90%] " src="/static/menu.png">
                            
                        </button>
                    </div>
                    <div class="menu z-10 hidden absolute left-20 w-[100px] mt-3 rounded border bg-white">
                        <ul>
                            <li class="rounded-t hover:bg-pink-400 hover:text-white  font-semibold font-mono  px-2 py-2"><a href="">Edit</a></li>
                            <li class="rounded-b hover:bg-pink-400 hover:text-white font-semibold font-mono  px-2 py-2 delete">Delete</li>
                            <li class="rounded-b hover:bg-pink-400 hover:text-white font-semibold font-mono  px-2 py-2"><a href="${viewUrl}">View</a></li>
                        </ul>
                    </div>
                </div>
            
            `
            wrapper.innerHTML += item


            
                
        }
        

        for (let i in data) {
            const btns = document.getElementsByClassName("btn");
            const menus = document.getElementsByClassName("menu");

            const btn = btns[i]
            const menu = menus[i]

            if (btn && menu) {

                btn.addEventListener("click", (e) => {
                    e.stopPropagation();
                    menu.classList.toggle("hidden");
                });
                document.addEventListener("click", (e) => {
                    if (!menu.contains(e.target) && !btn.contains(e.target)) {
                        menu.classList.add("hidden");
                    }

                })
            }




            
            
            
        }
        const delbtns = document.getElementsByClassName("delete");
        for (let i in delbtns) {
            if (isNaN(i)) continue
            delbtns[i].addEventListener('click', (function () {
                let pin = data[i]
                delbtn(pin)
                list()


            }))
        }

        
        

    }
        
        
            
    list();  
}

if(PinView){
    async function view() {
        let url = "http://127.0.0.1:8000/api/list/";
        let response = await fetch(url)
        let data = await response.json()
        

        const viewPin = document.getElementsByClassName("view");
        for (let i in data) {
            if (isNaN(i)) continue
            viewPin[i].addEventListener("click", (function () {
                
                let pin = data[i]
                console.log(pin)

            }))

            // for (id in pinid){
            //     
            // }

            
        //     // 
        


        //     // 
        }
        
    }
    view()
}



    

    


function delbtn(item) {
    let id = item.id
    console.log('deleted item clicked', item)
    let url = `http://127.0.0.1:8000/api/delete/${id}/`
    fetch(url, {
        method: "DELETE",
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        }
    }).then(resp => {
       list()
    })
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


async function getuser() {
    let url2 = 'http://127.0.0.1:8000/api/getUser/'
    let resp2 = await fetch(url2)
    let userdata = await resp2.json()
    let user = userdata.username
    return user
}
const user = getuser()

let form = document.getElementById("form")
if (form){


form.addEventListener('submit', (e) => {
    e.preventDefault()
    let file = document.getElementById("file").files[0]
    let title = document.getElementById("title").value
    let url = "http://127.0.0.1:8000/api/create/"

    


    let formData = new FormData()
    formData.append('image', file)
    formData.append('title', title)
    formData.append('author', user)




    fetch(url, {
        method: "POST",
        headers: {
            'X-CSRFToken': csrftoken,
        },
        body: formData,
    })
        .then(resp => resp.json())
        .then(data => {
            alert('Posted');
            list(); 
            document.getElementById("title").value = "";
           
        })


})

}


// function displaymenu(){
//     if (btn && menu) {
//         btn.addEventListener("click", (e) => {
//             e.stopPropagation();
//             menu.classList.toggle("hidden");
//         });

//         document.addEventListener("click", (e) => {
//             if (!menu.contains(e.target) && !btn.contains(e.target)) {
//                 menu.classList.add("hidden");
//             }
//         });

//     }
// }












// async function pinView(item) {
//     let id = item.id
//     console.log(`Hello id no ${id}`)


//     let url = `http://127.0.0.1:8000/api/view/${id}/`
//     let response = await fetch(url)
//     let data = await response.json()
//     console.log(data)


//     let pin = `
//     <div class="z-2 p-5 border w-[500px]  h-[500px] bg-pink-200 rounded-2xl flex  items-center gap-4 justify-between">

//     <img class="rounded-2xl w-[250px] h-full" src=${data.img_url}>
//     <div class="flex w-[200px] h-full  items-end">
//         <div class="flex flex-col bg-slate-200 p-2 rounded-b-2xl items-end pb-5">

//             <p class="text-[19px] font-semibold text-gray-700 text-end">${data.title}</p>
//             <small class="mt-3 text-sm font-bold text-end">${data.author}</small>

//         </div>
//     </div>
// </div>
//     `
//     PinView.innerHTML += pin


// }