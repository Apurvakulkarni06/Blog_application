$( '.nav-wrapper #nav-mobile a' ).on( 'click', function () {
	$( '.nav-wrapper #nav-mobile' ).find( 'li.active' ).removeClass( 'active' );
	$( this ).parent( 'li' ).addClass( 'active' );
});