(function( $ ) {

  console.clear()
  console.log('svgColor')

  var mainHolder, colorHolder
  var btnRandom, btnClear, btnDownloadSVG, btnDownloadPNG
  var svgObject, svgOutline, svgColor
  var swatchUp, swatchDown
  var fillSpeed = 0.15
  var chosenColor = '#FFFFFF'
  var colors = ['#FFFFFF', '#8E53A1', '#6ABD46', '#71CCDC', '#F7ED45', '#F7DAAF', '#EC2527', '#F16824', '#CECCCC', '#5A499E', '#06753D', '#024259', '#FDD209', '#7D4829', '#931B1E', '#B44426', '#979797', '#C296C5', '#54B948', '#3C75BB', '#F7ED45', '#E89D5E', '#F26F68', '#F37123', '#676868', '#9060A8', '#169E49', '#3CBEB7', '#FFCD37', '#E5B07D', '#EF3C46', '#FDBE17', '#4E4D4E', '#6B449B', '#BACD3F', '#1890CA', '#FCD55A', '#D8C077', '#A62E32', '#F16A2D', '#343433', '#583E98', '#BA539F', '#9D2482', '#DD64A5', '#DB778D', '#EC4394', '#E0398C', '#68AF46', '#4455A4', '#FBEE34', '#AD732A', '#D91E36', '#F99B2A']
  var closeOffset

  function swatchClick(){
    chosenColor = $(this).data('color')
    console.log(chosenColor)
    TweenMax.to(colorHolder, fillSpeed, { backgroundColor:chosenColor })
  }
  function swatchMove(e){
    var moveTo = (e.type == 'mouseenter')? swatchUp: swatchDown;
    TweenMax.to('.swatchHolder', 0.5, moveTo);
  }

  function colorMe() {
    TweenMax.to(this, fillSpeed, { fill: chosenColor });
  }
  function colorRollover(e){
    var rollover = (e.type == 'mouseenter')? {scale:1.2}:{scale:1};
    TweenMax.to($(this), 0.05, rollover);
  }

  function svgRandom() {
    $(svgColor).each(function(){
      var randomNum = Math.floor((Math.random() * colors.length) + 1);
      TweenMax.to(this, fillSpeed, { fill: colors[randomNum] });
    })
  }
  function svgClear() {
    $(svgColor).each(function(){
      TweenMax.to(this, fillSpeed, { fill: "#FFF" });
    })
  }
  function svgDownloadSVG() {
   var svgInfo = $("<div/>").append($(svgObject).clone()).html();
   $(this).attr({
            href:"data:image/svg+xml;utf8,"+svgInfo,
            download:'coloringBook.svg',
            target:"_blank"
    });
  }
  function svgDownloadPNG() {
   // Future expantion:
   // Look at https://bl.ocks.org/biovisualize/8187844
  }

  $.fn.makeSwatches = function() {
    var swatchHolder = $('<ol/>', {'class': 'swatchHolder'}).appendTo(this)
        colorHolder  = $('<li/>', {'class': 'colorHolder', 'text':'Current Color'}).css('background-color', chosenColor).appendTo(swatchHolder)

    $.each(colors, function() {
      var swatch = $('<li/>').appendTo(swatchHolder)
      $(swatch).css('background-color', this)
      $(swatch).data('color', this)
      $(swatch).on('click', swatchClick)
      $(swatch).on('mouseenter mouseleave', colorRollover)
    })

    var swatchPos = $('.colorHolder').position()
    var swatchHeight = $('.colorHolder').outerHeight(true) + swatchPos.top
    closeOffset = swatchHeight - $('.swatchHolder').outerHeight()

    $('.swatchHolder').on('mouseenter mouseleave', swatchMove)
    $('.swatchHolder').css('bottom',closeOffset)
    swatchUp   = {css:{bottom:0}}
    swatchDown = {css:{bottom:closeOffset}}
  }
  $.fn.makeSVGcolor = function(svgURL) {
    mainHolder = this
    $( this ).load(svgURL, function() {
      svgObject  = $('svg', this)
      svgColor   = $('g:nth-child(2)', svgObject).children()
      svgOutline = $('g:nth-child(1)', svgObject).children()
      $(svgColor).on('click', colorMe)
      $(mainHolder).makeSwatches()
      $('.swatchHolder').addClass('gray')
    });
  }

  $.fn.btnRandom    = function() {
    btnRandom = this
    $(btnRandom).on('click', svgRandom)
  }
  $.fn.btnClear     = function() {
    btnClear = this
    $(btnClear).on('click', svgClear)
  }
  $.fn.btnDownload  = function(type) {
    if(type == 'PNG'){
      btnDownloadPNG = this
      $(this).on('mouseenter', svgDownloadPNG)
    } else {
      btnDownloadSVG = this
      $(this).on('mouseenter', svgDownloadSVG)
    }
  }
}( jQuery ));

$('#ActivityDIV'   ).makeSVGcolor('https://s3-us-west-2.amazonaws.com/s.cdpn.io/40041/cheshire.svg')
$('#btnRandom'     ).btnRandom()
$('#btnClear'      ).btnClear()
$('#btnDownloadSVG').btnDownload()