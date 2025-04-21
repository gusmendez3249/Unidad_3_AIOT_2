function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const humedad1 = data.humedad1;
    const humedad2 = data.humedad2;
    const humedad3 = data.humedad3;
    const estadoRiego = data.estadoRiego;
    const email = "gustavoangelc2005@gmail.com";
    
    // Verificar si al menos una maceta tiene humedad baja (<40%)
    if (humedad1 < 40 || humedad2 < 40 || humedad3 < 40) {
      // Crear HTML para un email con mejor diseño
      const htmlBody = `
      <!DOCTYPE html>
      <html>
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Alerta de Riego</title>
      </head>
      <body style="margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
        <div style="max-width: 600px; margin: 0 auto; background-color: #f5f5f5; padding: 20px;">
          <!-- Encabezado -->
          <div style="background: linear-gradient(135deg, #16a085 0%, #27ae60 100%); color: white; padding: 20px; text-align: center; border-radius: 10px 10px 0 0;">
            <h1 style="margin: 0; font-size: 24px;">💧 ALERTA DE RIEGO AUTOMÁTICO</h1>
          </div>
          
          <!-- Contenido principal -->
          <div style="background-color: white; padding: 20px; border-radius: 0 0 10px 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
            <p style="font-size: 16px; color: #555; line-height: 1.5;">El sistema ha detectado niveles bajos de humedad en sus plantas y ha activado el riego automático.</p>
            
            <!-- Maceta 1 -->
            <div style="margin: 25px 0; border-left: 4px solid ${humedad1 < 40 ? '#e74c3c' : '#16a085'}; padding-left: 15px;">
              <h3 style="margin: 0; color: #333;">🪴 Maceta 1</h3>
              <div style="display: flex; align-items: center; margin-top: 10px;">
                <div style="flex-grow: 1; background-color: #eee; height: 10px; border-radius: 5px; overflow: hidden;">
                  <div style="width: ${humedad1}%; height: 100%; background: ${
        humedad1 < 30 ? '#e74c3c' : 
        humedad1 < 40 ? '#f39c12' : 
        humedad1 < 70 ? '#3498db' : '#16a085'
      };"></div>
                </div>
                <span style="margin-left: 10px; font-weight: bold; color: ${
                  humedad1 < 30 ? '#e74c3c' : 
                  humedad1 < 40 ? '#f39c12' : 
                  humedad1 < 70 ? '#3498db' : '#16a085'
                };">${humedad1}%</span>
              </div>
            </div>
            
            <!-- Maceta 2 -->
            <div style="margin: 25px 0; border-left: 4px solid ${humedad2 < 40 ? '#e74c3c' : '#16a085'}; padding-left: 15px;">
              <h3 style="margin: 0; color: #333;">🪴 Maceta 2</h3>
              <div style="display: flex; align-items: center; margin-top: 10px;">
                <div style="flex-grow: 1; background-color: #eee; height: 10px; border-radius: 5px; overflow: hidden;">
                  <div style="width: ${humedad2}%; height: 100%; background: ${
        humedad2 < 30 ? '#e74c3c' : 
        humedad2 < 40 ? '#f39c12' : 
        humedad2 < 70 ? '#3498db' : '#16a085'
      };"></div>
                </div>
                <span style="margin-left: 10px; font-weight: bold; color: ${
                  humedad2 < 30 ? '#e74c3c' : 
                  humedad2 < 40 ? '#f39c12' : 
                  humedad2 < 70 ? '#3498db' : '#16a085'
                };">${humedad2}%</span>
              </div>
            </div>
            
            <!-- Maceta 3 -->
            <div style="margin: 25px 0; border-left: 4px solid ${humedad3 < 40 ? '#e74c3c' : '#16a085'}; padding-left: 15px;">
              <h3 style="margin: 0; color: #333;">🪴 Maceta 3</h3>
              <div style="display: flex; align-items: center; margin-top: 10px;">
                <div style="flex-grow: 1; background-color: #eee; height: 10px; border-radius: 5px; overflow: hidden;">
                  <div style="width: ${humedad3}%; height: 100%; background: ${
        humedad3 < 30 ? '#e74c3c' : 
        humedad3 < 40 ? '#f39c12' : 
        humedad3 < 70 ? '#3498db' : '#16a085'
      };"></div>
                </div>
                <span style="margin-left: 10px; font-weight: bold; color: ${
                  humedad3 < 30 ? '#e74c3c' : 
                  humedad3 < 40 ? '#f39c12' : 
                  humedad3 < 70 ? '#3498db' : '#16a085'
                };">${humedad3}%</span>
              </div>
            </div>
            
            <!-- Estado del Riego -->
            <div style="background-color: ${estadoRiego ? '#e8f5e9' : '#ffebee'}; padding: 15px; border-radius: 8px; margin-top: 20px;">
              <h3 style="margin: 0; color: ${estadoRiego ? '#2e7d32' : '#c62828'};">
                🚿 Estado del sistema de riego: <span style="font-weight: bold;">${estadoRiego ? 'ACTIVADO' : 'DESACTIVADO'}</span>
              </h3>
            </div>
            
            <!-- Fecha y hora -->
            <p style="margin-top: 25px; color: #777; font-size: 14px; text-align: right;">
              📅 ${new Date().toLocaleString('es-ES', {
                weekday: 'long',
                year: 'numeric',
                month: 'long',
                day: 'numeric',
                hour: '2-digit',
                minute: '2-digit'
              })}
            </p>
          </div>
          
          <!-- Pie de página -->
          <div style="text-align: center; padding: 15px; color: #666; font-size: 12px;">
            <p>Este es un mensaje automático del sistema de riego inteligente.</p>
          </div>
        </div>
      </body>
      </html>
      `;
      
      // Texto plano alternativo
      const textBody = 
        "💧 ALERTA DE HUMEDAD BAJA - RIEGO ACTIVADO\n\n" +
        "🪴 Humedad Maceta 1: " + humedad1 + "%\n" +
        "🪴 Humedad Maceta 2: " + humedad2 + "%\n" +
        "🪴 Humedad Maceta 3: " + humedad3 + "%\n" +
        "🚿 Estado del sistema de riego: " + (estadoRiego ? "Activado" : "Desactivado") + "\n" +
        "📅 Fecha y hora: " + new Date().toLocaleString();
      
      // Enviar email
      MailApp.sendEmail({
        to: email,
        subject: "🌱 ALERTA: Sistema de Riego Activado",
        htmlBody: htmlBody,
        body: textBody
      });
      
      return ContentService.createTextOutput("Correo de riego enviado").setMimeType(ContentService.MimeType.TEXT);
    } else {
      return ContentService.createTextOutput("Humedad suficiente, no se activa riego").setMimeType(ContentService.MimeType.TEXT);
    }
    
  } catch (error) {
    return ContentService.createTextOutput("Error: " + error.message).setMimeType(ContentService.MimeType.TEXT);
  }
}