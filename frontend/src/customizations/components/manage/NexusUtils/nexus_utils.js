// Simula una llamada a IA que devuelve un string para actualizar el campo 'title'
export const simulateIACall = () => {
    return new Promise(resolve => {
      setTimeout(() => {
        resolve("Nuevo Título desde la IA");
      }, 1000); // Simula una respuesta después de 1 segundo
    });
  }
  
  // Función para manejar el click del botón que interactúa con la IA
  export const fetchAIResponse = async (propes) => {
    const formData = propes.globalData;
    const title = formData.title; // Obtener el título desde formData
    const dashboardId = formData.dashboard_id; // Obtener dashboard_id desde formData

    console.log("Botón de Presentación clickeado para:", propes);
       
    alert("Hola mundo desde la presentación: " + title + ", Dashboard ID: " + dashboardId);
    return("non shalarius");
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