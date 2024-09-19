import axios from 'axios';


// Simula una llamada a IA que devuelve un string para actualizar el campo 'title'
export const simulateIACall = () => {
    return new Promise(resolve => {
      setTimeout(() => {
        resolve("Nuevo Título desde la IA");
      }, 1000); // Simula una respuesta después de 1 segundo
    });
  }
  
  // Función para manejar el click del botón que interactúa con la IA
  export const fetchAIResponse = async (propes,eltype, action) => {
    const url = 'http://localhost:8000/aidDexterity';
    const headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
    };
    const processedFormData = {};
    const fieldsToRemove = ['contributors', 'creators', 'effective', 'expires', 'subjects', 'parent','language','rights'];
    const formData = propes.globalData;
    const title = formData.title; // Obtener el título desde formData
    const dashboardId = formData.dashboard_id; // Obtener dashboard_id desde formData
    
    Object.keys(formData).forEach(key => {
    // Verificar si el campo debe ser eliminado y si está undefined
    //|| formData[key] !== undefined
     if (!fieldsToRemove.includes(key) ) {
       // Convertir undefined a null (o puedes usar una cadena vacía "")
      processedFormData[key] = formData[key] === undefined ? null : formData[key];
      }
     });
    const jsonString = JSON.stringify(processedFormData);
    //console.log("procesedForm",processedFormData);
    //console.log("propesid",propes['datasource']['@id'] );
    //processedFormData['dataset']=propes['datasource']['@id'];
    //console.log("json", propes)
    //console.log("eltype", eltype)
    //console.log("accion", action)
    try {
    const response = await axios.post(url, {
      tipo: eltype.toString(),
      accion: action.toString(),
      data:processedFormData
    }, { headers: headers })
       
        //console.log('Respuesta recibida:', response.data, response.data.query,response.data.base_de_datos);
        //elqry=response.data.query;
        //elbd=response.data.database;
        alert("Hola mundo desde la presentación: " + jsonString + ", Dashboard ID: " + action);
        try {
        if (eltype == "tabla_auxiliar"){
          return {
            campo: response.data.query,
            base_de_datos: response.data.base_de_datos
        };
       }
        else {
          return {
            campo: null,
            base_de_datos: null,
        };
    }
  } catch (error) {
    console.error("Error fetching data:", error);
    return { 
        campo: null, 
        base_de_datos: null
    };
}
    } catch(error) {
        console.error('Error en la llamada API:', error);
      }
    
      
    
  }

  
export const handlePresentationButtonClick = (propes) => { // Agregar parámetro formData
    const formData = propes.globalData;
    const title = formData.title; // Obtener el título desde formData
    const dashboardId = formData.dashboard_id; // Obtener dashboard_id desde formData

    console.log("Botón de Presentación clickeado para:", propes);
       
    alert("Hola mundo desde la presentación: " + title + ", Dashboard ID: " + dashboardId);
    return("non shalarius");
};


export const handlePresentationButtonClick2 = (content) => {
    const title = content.title; 
    const dashboard = content.dashboard_id;
  
    console.log("Botón de Presentación clickeado para:", content); 
    alert("Hola mundos desde la presentación: " + title +  dashboard); 
  };