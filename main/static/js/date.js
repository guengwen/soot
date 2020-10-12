// Call the dataTables jQuery plugin


$(document).ready(function() {
  var table = $('#dataTable').DataTable({
    dom: 'lBfrtip',
    buttons: {
      dom: {
        button: {
          tag: 'button',
          className: ''
        }
      },
      buttons: [{
        extend: 'excel',
        className: 'btn btn-sm btn-success',
        titleAttr: 'Excel export.',
        text: 'Excel',
        filename: 'excel-export',
        extension: '.xlsx'
      }],
    }
  });

  $("#min").datepicker({ onSelect: function () { table.draw(); }, changeMonth: true, changeYear: true });
  $("#max").datepicker({ onSelect: function () { table.draw(); }, changeMonth: true, changeYear: true });

  $('#min, #max').change(function () {
      table.draw();
  });
} );

$(document).ready(function(){

  var btns = $('.buttons-excel');
  btns.css("margin-left","20px");
  btns.css("margin-top","-2px")

});


$(document).ready(function(){
  $.fn.dataTable.ext.search.push(
  function (settings, data, dataIndex) {
      var min = $('#min').datepicker("getDate");
      var max = $('#max').datepicker("getDate");
      var startDate = new Date(data[14]);
      if (min == null && max == null) { return true; }
      if (min == null && startDate <= max) { return true;}
      if(max == null && startDate >= min) {return true;}
      if (startDate <= max && startDate >= min) { return true; }
      return false;
  });
});


$.fn.dataTableExt.afnFiltering.push(
	 function (settings, data, dataIndex) {
        var FilterStart = $('#min').val();
        var FilterEnd = $('#max').val();
        var DataTableStart = data[4].trim();
        var DataTableEnd = data[5].trim();
        if (FilterStart == '' || FilterEnd == '') {
            return true;
        }
        if (DataTableStart >= FilterStart && DataTableEnd <= FilterEnd)
        {
            return true;
        }
        else {
            return false;
        }
        
    });
    --------------------------
 $('#min').change(function (e) {
        Table.draw();

    });
    $('#max').change(function (e) {
          Table.draw();

    });
