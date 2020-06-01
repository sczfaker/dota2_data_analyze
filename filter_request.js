if (oSession.HostnameIs("域名") && oSession.uriContains("期望字符")){  
            var filename = "D:/workspace/.../request.log";  
            var curDate = new Date();  
            var logContent =  "[" + curDate.toLocaleString() + "] " + oSession.PathAndQuery + "\r\n";  
            var sw : System.IO.StreamWriter;  
            if (System.IO.File.Exists(filename)){  
                sw = System.IO.File.AppendText(filename);  
                sw.Write(logContent);  
            }  
            else{  
                sw = System.IO.File.CreateText(filename);  
                sw.Write(logContent);  
            }  
            sw.Close();  
            sw.Dispose();  
        } 
