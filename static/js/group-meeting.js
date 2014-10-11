function changeProject(targetId, contentId, projectId) {
    $('#' + targetId).load("/?pid=" + projectId + " #" + contentId);
}