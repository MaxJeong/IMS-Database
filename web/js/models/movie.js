splat.Movie = Backbone.Model.extend({
    // match localStorage (later server DB) use of _id, rather than id
    idAttribute: "_id",
    url: "http://mathlab.utsc.utoronto.ca:41302/movies",

    defaults: {
		title: "",
		release: null,
		director: "",
		starring: [],
		rating: "",
		duration: null,
		genre: [],
		synopsis: "",
		freshTotal: 0.0,
		freshVotes: 0.0,
		trailer: "mpv/default.mp4",
		poster: "img/default.png",
		date: new Date(),
    },

    validateCheck:function(item){
    	console.log(item.attr('name'));
		if (item.attr('name') == 'title') {
			if ((item.val()).match(/[a-z0-9]+[\,\.\!\?\-\'\*]*/i)) {
				return true;
			}
		}
		else if (item.attr('name') == 'released') {
			if ((item.val()) >= 1910 && (item.val()) <= 2016) {
				return true;
			}
		}
		else if (item.attr('name') == 'director') {
			if ((item.val()).match(/[a-z]+[0-9]*[\,\.\!\?\-\'\*]*/i)) {
				return true;
			}
		}
		else if (item.attr('name') == 'starring') {
			if ((item.val()).match(/[a-z]+[\sa-z, \-\']*/i)) {
				return true;
			}
		}
		else if (item.attr('name') == 'genre') {
			if ((item.val()).match(/[a-z]+[\sa-z, \-\']*/i)) {
				return true;
			}
		}
		else if (item.attr('name') == 'rating') {
			if (item.val() == 'G' || item.val() == 'PG'
				|| item.val() == 'PG-13' || item.val() == 'R'
				|| item.val() == 'NC-17') {
				return true;
			}
		}
		else if (item.attr('name') == 'duration') {
			if ((item.val()) >= 0 && (item.val()) <= 999) {
				return true;
			}
		}
		else if (item.attr('name') == 'synopsis') {
			if ((item.val()).match(/\w/g)) {
				return true;
			}
		}
		else if (item.attr('name') == 'chosenimg') {
			if( true){

				return true;
			}
		}
		else if (item.attr('name') == 'trailer') {
			if (((item.val()).substring(0, 11) == 'http://www.' &&
				((item.val()).substring(((item.val()).length)-4, 
					(item.val()).length)).match('.com|.org'))
					|| (item.val()) == '') {
				return true;
			}
		}
		return false;
	},

});
