<div class="row">
    <div class="col-xs-6">  <!-- col 1 -->
        <div id="movieform" class = "input-append ">
        	<div class="editActions">
    			<input type="button" id="moviesave"
		   		class="btn btn-primary save"
		   		name="save" value="Save Changes"/>
	    		<input type="button" id="moviedel"
		   		class="btn btn-danger delete"
		   		name="delete" value="Delete Movie"/>
			</div>

			<div class="form-horizontal">
	   			<div class="form-group">
	       			<label for="title" class="col-sm-3 control-label">Title</label>
	       			<input type="text" style="color: black" class="col-sm-9"
	                placeholder="e.g. Day of the Jackal"
	                name="title" value=""/>
	   			</div>
	   			<div class="form-group">
	   				<label for="released" class="col-sm-3 control-label">Released</label>
	       			<input type="text" style="color: black" class="col-sm-9"
	       			placeholder="e.g. 1969"
	       			name="released" value=""/>
	   			</div>
	   			<div class="form-group">
	   				<label for="director" class="col-sm-3 control-label">Director</label>
	       			<input type="text" style="color: black" class="col-sm-9"
	       			placeholder="e.g. Steven Spellberg"
	       			name="director" value=""/>
	   			</div>
	   			<div class="form-group">
	   				<label for="rating" class="col-sm-3 control-label">Rating</label>
	       			<input type="text" style="color: black" class="col-sm-9"
	       			placeholder="e.g. G, PG, PG-13, R"
	       			name="rating" value=""/>
	   			</div>
	   			<div class="form-group">
	   				<label for="starring" class="col-sm-3 control-label">Starring</label>
	       			<input type="text" style="color: black" class="col-sm-9"
	       			placeholder="e.g. Steve Martin"
	       			name="starring" value=""/>
	   			</div>
	   			<div class="form-group">
	   				<label for="duration" class="col-sm-3 control-label">Duration</label>
	       			<input type="text" style="color: black" class="col-sm-9"
	       			placeholder="e.g. 122 minutes"
	       			name="duration" value=""/>
	   			</div>
	   			<div class="form-group">
	   				<label for="genre" class="col-sm-3 control-label">Genre(s)</label>
	       			<input type="text" style="color: black" class="col-sm-9"
	       			placeholder="e.g. Comedy, thriller, action"
	       			name="genre" value=""/>
	   			</div>
	   			<div class="form-group">
	   				<label for="synopsis" class="col-sm-3 control-label">Synopsis</label>
	       			<input type="text" style="color: black" class="col-sm-9"
	       			placeholder="summary of the movie plot"
	       			name="synopsis" value=""/>
	   			</div>
	   			<div class="form-group">
	   				<label for="trailer" class="col-sm-3 control-label">Trailer URL</label>
	       			<input type="text" style="color: black" class="col-sm-9"
	       			placeholder="e.g. https://www.archive.org"
	       			name="trailer" value=""/>
	   			</div>
			</div>
        </div>
    </div>  <!-- end column 1 -->

    <div class="col-xs-6">  <!-- col 2 -->
		<div id='img_pic' class="dropzone">
    			<img id='displayimg' src="./img/default.png" alt="Default Poster" >
		</div>
        <input type="file" id="imgsave" accept="image/*" capture class="btn btn-primary save" name="chosenimg" value="Choose File or snap a photo!"/>
    </div>   <!-- end column 2 -->
</div> <!-- row -->
