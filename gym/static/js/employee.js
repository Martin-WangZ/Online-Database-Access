$(()=>{
    $("#select").click(
        ()=>{
            $("#table").empty();
           $.post(
               '/employee_select',
               {
                   eid:$("#eid").val()
               },
               (json)=>{
                   th="<tr>\n" +
                       "<th>Employee ID</th>\n" +
                       "<th>UserName</th>\n" +
                       "<th>Email</th>\n" +
                       "<th>Phone</th>\n" +
                       "<th>Salary</th>\n" +
                       "<th>Is_internship</th>\n"+
                       "</tr>";
                   $("#table").append(th);
                   json.forEach(
                       (row)=>{
                            $("#table").append(
                                "<tr><td>"+row.eid+"</td><td>"+
                                row.username+"</td><td>"+row.email+"</td><td>"+
                                row.phone+"</td><td>"+row.salary+"</td><td>"+
                                row.is_internship+"</td></tr>"
                            )
                       }
                   );
               }
           )
        }
    );

$("#delete").click(
        ()=>{
            if($("#eid").val()==""){
                alert("please input eid to delete")
            }
            else {
                $.getJSON(
                '/employee_delete',
                {
                    eid:$("#eid").val()
                },
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

$("#update").click(
        ()=>{
            if($("#eid").val()==""&& $("#username").val()==""&& $("#email").val()==""&& $("#phone").val()=="" && $("#salary").val()=="" && $("#is_internship").val()=="" && $("#password").val()==""){
                 alert("please input content!")
            }
            $.getJSON(
                '/employee_update',
                {
                    eid:$("#eid").val(),
                    username:$("#username").val(),
                    email:$("#email").val(),
                    phone:$("#phone").val(),
                    salary:$("#salary").val(),
                    is_internship:$("#is_internship").val(),
                    password:$("#password").val()
                },
                (json)=>{
                    if(json.status==1)
                        alert("update success!")
                    if(json.status==0)
                        alert("update fail please use correct employee ID")
                }
            )
        }
    );


})