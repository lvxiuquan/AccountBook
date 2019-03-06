/*
 * utf-8
 */

if (typeof (main) == 'undefined') {
    main = {};
}

main.base = {
    submitAccount: function(){
        var push_data = new Object();
        push_data.description = $("#description").val();
        push_data.amount = $("#amount").val();
        push_data.time = $("#time").val();
        push_data.amount_1 = $("#amount_1").val();
        push_data.amount_2 = $("#amount_2").val();
        push_data.amount_3 = $("#amount_3").val();
        push_data.amount_4 = $("#amount_4").val();

        if(push_data.description.length == 0){
            alert("消费内容不能为空");
            $('#description').focus();
            return false
        }
        if(push_data.amount.length == 0 || isNaN(push_data.amount)){
            alert("请填写花费金额");
            $('#amount').focus();
            return false
        }
        if(push_data.time.length == 0){
            alert("请填写消费时间");
            $('#time').focus();
            return false
        }
        $.ajax({
            type:'POST',
            url:'/account/submit_account.ajax',
            data: {"push_data": JSON.stringify(push_data),},
            dataType : "json",
            success: function(data) {
                if(data["status"] == 0){
                    location.reload();
                }else{
                    alert(data["message"]);
                }
            },
            error: function(e) {
               alert("操作失败,请稍后重新尝试或者联系管理员");
            }
        });
    },
    share: function(){
        var amount = $("#amount").val();
        var checked_list = $(".user_check");
        var count = parseInt($(".user_check:checked").length);
        if (count == 0) {
            alert("至少要有一个参与人");
            return false
        };
        $(checked_list).each(function(){
            var id = $(this).attr("data-id");
            if ($(this).attr("checked")) {
                $("#"+id).val(parseInt(amount)/count)
            }else{
                $("#"+id).val(0)
            }
        })
    },
    filter: function(obj){
        var key_val = $(obj).val();
        $(".filter_tb tr").each(function(){
            var tmp_flag = 0
            $(this).find('td').each(function(){ 
                if($(this).html().toLowerCase().indexOf(key_val.toLowerCase()) > -1){
                    tmp_flag = 1
                }
            });
            if(tmp_flag == 1){
                $(this).show();
            }else{
                $(this).hide();
            }
        });
    },
}

$(function(){
    $("#amount").keyup(function(){
        $(".amount").val("0");
        var amount = $(this).val();
        if(amount.length == 0){return false;}
        if(isNaN(amount)){
            alert("请填写正确的金额");
            $('#amount').val("").focus();
            return false
        }
        main.base.share();
    });
    $(".user_check").click(function(){
        main.base.share();
    });
});
