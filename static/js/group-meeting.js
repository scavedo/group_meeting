function changeProject(targetId, contentId, projectId) {
    $('#' + targetId).load("/?pid=" + projectId + " #" + contentId);
}

function loadCalendar(projectId) {
    $('#view_content').load("calendar/?pid=" + projectId);
}

function loadNotes(projectId) {
    $('#view_content').load("notes/?pid=" + projectId);
}

function loadFiles(projectId) {
    $('#view_content').load("files/?pid=" + projectId);
}

function loadHome(projectId) {
    $('#view_content').load("project-home/?pid=" + projectId);
}

function deleteNote(id) {
    $('#noteModal').load('delete-note/?nid=' + id, function() {
        $('#noteModal').attr('data-id', id);
        $('#myModal').modal("show");
    });
}

function deleteFile(id) {
    $('#fileModal').load('delete-file/?fid=' + id, function() {
        $('#fileModal').attr('data-id', id);
        $('#myModal').modal("show");
    });
}

function deleteMeeting(id) {
    $('#meetingModal').load('delete-meeting/?mid=' + id, function() {
        $('#meetingModal').attr('data-id', id);
        $('.popover').popover('destroy');
        $('#myModal').modal("show");
    });
}