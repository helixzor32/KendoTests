var id = 1;
var griddata = '';
function createRandomData(count) {
	//Set up data query
	/*$.getJSON('http://127.0.0.1:8000/employees/query', function(data) {
		var emps = [];
		$.each(data, function(key, val) {
			var fields = val.fields;
			//Parse out individual items
			var fname = fields.fname;
			var lname = fields.lname;
			var city = fields.city;
			var title = fields.title;
			var dob = fields.dob;
			dob = dob.substring(0,10);
			var tempid = id;
			var age = fields.age;
			griddata.push({
				Id: id,
				FirstName: fname,
				LastName: lname,
				City: city,
				Title: title,
				BirthDate: dob,
				Age: age
			});
			id++;
		});
		//Assign JSON to var
		griddate = data;
		
		//Clear html
		$("#grid").html("");*/
		
		
	//});
}

function generatePeople(itemCount, callback) {
    var data = [],
        delay = 25,
        interval = 500,
        starttime;

    var now = new Date();
    setTimeout(function() {
        starttime = +new Date();
        do {
            var firstName = firstNames[Math.floor(Math.random() * firstNames.length)],
                lastName = lastNames[Math.floor(Math.random() * lastNames.length)],
                city = cities[Math.floor(Math.random() * cities.length)],
                title = titles[Math.floor(Math.random() * titles.length)],
                birthDate = birthDates[Math.floor(Math.random() * birthDates.length)],
                age = now.getFullYear() - birthDate.getFullYear();

            data.push({
                Id: data.length + 1,
                FirstName: firstName,
                LastName: lastName,
                City: city,
                Title: title,
                BirthDate: birthDate,
                Age: age
            });
        } while(data.length < itemCount && +new Date() - starttime < interval);

        if (data.length < itemCount) {
            setTimeout(arguments.callee, delay);
        } else {
            callback(data);
        }
    }, delay);
}
