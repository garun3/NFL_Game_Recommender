var select, i, option;

select = document.getElementById( 'test' );

for ( i = 12; i <= 100; i += 1 ) {
    for (var age = 12; age <= 100; age++) {
        select.add(new Option(age));
      }
}