$(()=>{
    $("#insert").click(
        ()=>{
            if($("#mid").val()==""&&$("#username").val()==""&&$("#password").val()==""&&$("#phone").val()==""&&$("#bid").val()==""&&$("#mtype").val()){
                alert("please input content!")
            }
            else {
                           $.post(
       '/member_insert',
       {
           mid:$("#mid").val(),
           username:$("#username").val(),
           password:$("#password").val(),
           phone:$("#phone").val(),
           bid:$("#bid").val(),
           mtype:$("#mtype").val()
       },
       (json)=>{
            if(json.status==1)
                        alert("insert success");
                    if(json.status==0)
                        alert("insert error please check your input")
       }
   );
            }

        }
    )


   $("#delete").click(()=>{
       if($("#mid").val()==""){
           alert("please input mid to delete!")
       }
       else {
           $.getJSON(
           '/member_delete?mid='+$("#mid").val(),
           (json)=>{
             if(json.status==1)
                 alert("delete success")
             if(json.status==0)
                 alert("delete fail please try again!")
           }
       )
       }
   });

    $("#update").click(()=>{
        if($("#mid").val()==""&&$("#username").val()==""&&$("#password").val()==""&&$("#phone").val()==""&&$("#bid").val()==""&&$("#mtype").val()==""){
            alert("please input content !")
        }
        else {
            $.post(
            '/member_update',
            {
                mid:$("#mid").val(),
                username:$("#username").val(),
                password:$("#password").val(),
                phone:$("#phone").val(),
                bid:$("#bid").val(),
                mtype:$("#mtype").val()
            },
            (json)=>{
                if(json.status==1)
                    alert("update success!")
                if(json.status==0)
                    alert("update fail please try again!")
            }
        )
        }
    });

    $("#select").click(()=>{
        $("#table").empty();
        $.getJSON(
            '/member_select?mid='+$("#mid").val(),
            (json)=>{
                if(json.status==1){
                    th="<tr>\n" +
                       "<th>First Name</th>\n" +
                       "<th>Last Name</th>\n" +
                       "<th>Branch ID</th>\n" +
                       "<th>Age</th>\n" +
                       "<th>Cost</th>\n" +
                       "</tr>";
                   $("#table").append(th);
                   json.all_rows.forEach(
                       (row)=>{
                            $("#table").append(
                                "<tr><td>"+row.fname+"</td><td>"+
                                row.lname+"</td><td>"+row.bid+"</td><td>"+
                                row.age+"</td><td>"+row.cost+"</td></tr>"
                            )
                       }
                   );
                }
                if(json.status==0)
                    alert("please input exist mid")
            }

        )
    })

})