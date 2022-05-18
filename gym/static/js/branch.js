
$(()=>{
    $("#select").click(
        ()=>{
            $("#table").empty();
           $.post(
               '/branch_select',
               {
                   bid:$("#bid").val()
               },
               (json)=>{
                   th="<tr>\n" +
                       "<th>Branch ID</th>\n" +
                       "<th>Branch Name</th>\n" +
                       "<th>Email</th>\n" +
                       "<th>Phone</th>\n" +
                       "<th>postcode</th>\n" +
                       "</tr>";
                   $("#table").append(th);
                   json.forEach(
                       (row)=>{
                            $("#table").append(
                                "<tr><td>"+row.bid+"</td><td>"+
                                row.bname+"</td><td>"+row.email+"</td><td>"+
                                row.phone+"</td><td>"+row.postcode+"</td></tr>"
                            )
                       }
                   );
               }
           )
        }
    );

    $("#insert").click(
        ()=>{
            if($("#bid").val()==""&& $("#bname").val()=="" && $("#email").val()=="" && $("#phone").val()=="" && $("#postcode").val()=="" ){
                     alert("please input !")
            }
            else{
               $.post(
                '/branch_insert',
                {
                    bid:$("#bid").val(),
                    bname:$("#bname").val(),
                    email:$("#email").val(),
                    phone:$("#phone").val(),
                    postcode:$("#postcode").val()
                },
                (json)=>{
                    if(json.status==1)
                        alert("insert success");
                    if(json.status==0)
                        alert("insert error please check your bid and postcode")


                }
            )

            }


        }
    );
    $("#delete").click(
        ()=>{
            if($("#bid").val()==""){
                alert("please input bid to delete!")
            }
            else {
                $.getJSON(
                '/branch_delete',
                {
                    bid:$("#bid").val()
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
            if($("#bid").val()==""&& $("#bname").val()=="" && $("#email").val()=="" && $("#phone").val()=="" && $("#postcode").val()==""){
                alert("please input content !")
            }
            else {
                $.getJSON(
                '/branch_update',
                {
                    bid:$("#bid").val(),
                    bname:$("#bname").val(),
                    email:$("#email").val(),
                    phone:$("#phone").val(),
                    postcode:$("#postcode").val()
                },
                (json)=>{
                    if(json.status==1)
                        alert("update success!")
                    if(json.status==0)
                        alert("update fail please use correct postcode or branch id")
                }
            )
            }

        }
    );



})