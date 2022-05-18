$(()=>{
    $("#insert").click(()=>{
      if($("#fid").val()==""&&$("#status_label").val()==""&&$("#manufactory").val()==""&&$("#manufacture_date").val()=="" && $("#eid").val()=="" && $("#is_outdoor").val()==""){
          alert("please input content !")
      }
      else {
          $.post(
          '/facility_insert',
          {
              fid:$("#fid").val(),
              status_label:$("#status_label").val(),
              manufactory:$("#manufactory").val(),
              manufacture_date:$("#manufacture_date").val(),
              eid:$("#eid").val(),
              is_outdoor:$("#is_outdoor").val()
          },
          (json)=>{
               if(json.status==1)
                   alert("insert success!")
              if(json.status==0)
                  alert("insert fail please input correct eid and fid !")
          }
      )
      }

    });

    $("#select").click(()=>{
        $("#table").empty();
        $.post(
            '/facility_select',
            {
                fid:$("#fid").val(),
                is_outdoor: $("#is_outdoor").val()
            },
            (json)=>{
                th="<tr>\n" +
                       "<th>Facility ID</th>\n" +
                       "<th>Status label</th>\n" +
                       "<th>Manufactory</th>\n" +
                       "<th>Manufacture_date</th>\n" +
                       "<th>Employee ID</th>\n" +
                       "<th>Is outdoor</th>\n" +
                       "</tr>";
                   $("#table").append(th);
                   json.forEach(
                       (row)=>{
                            $("#table").append(
                                "<tr><td>"+row.fid+"</td><td>"+
                                row.status_label+"</td><td>"+row.manufactory+"</td><td>"+
                                row.manufacture_date+"</td><td>"+row.eid+"</td><td>"+
                                row.is_outdoor+"</td></tr>"
                            )
                       }
                   );

            }

        )
    });



    $("#delete").click(
        ()=>{
            if($("#fid").val()==""){
                alert("please input fid !")
            }
            else {
                $.getJSON(
                '/facility_delete?fid='+$("#fid").val(),
                (json)=>{
                    if(json.status==1)
                        alert("delete success!")
                    else if(json.status==0)
                        alert("delete fail ! please try again")
                    else
                        alert("unknown error, please try again !")
                }
            )
            }
        }
    );

    $("#update").click(()=>{
      if($("#fid").val()==""&&$("#status_label").val()==""&&$("#manufactory").val()==""&&$("#manufacture_date").val()==""&&$("#eid").val()==""&&$("#is_outdoor").val()==""){
          alert("please input content !");
      }
      else {
          $.post(
          '/facility_update',
          {
              fid:$("#fid").val(),
              status_label:$("#status_label").val(),
              manufactory:$("#manufactory").val(),
              manufacture_date:$("#manufacture_date").val(),
              eid:$("#eid").val(),
              is_outdoor:$("#is_outdoor").val()
          },
          (json)=>{
               if(json.status==1)
                   alert("update success!")
              if(json.status==0)
                  alert("update fail please input correct eid and fid !")
          }
      )
      }
    });
})