

#' Create Github Top Languages Card
#'
#' @param username Your Github username
#' @param exclude_repo if not `NULL`, specify character vector of repo name(s) to exclude individual repositories.
#' @param hide if not `NULL`, specify character vector of language name(s) to hide
#' @param langs_count Option to specify the number of languages shown on the card, must be an integer from 1 to 10, default is 5.
#' @param layout_compact if `TRUE`, card will show in a compact layout
#'
#' @return A character rendering GitHub Top Languages Card to be inserted into R Markdown "github_document"
#' @export
#' @source https://github.com/anuraghazra/github-readme-stats
#'
gh_top_lang_card <- function(username,
                             exclude_repo = NULL,
                             hide = NULL,
                             langs_count = 5,
                             layout_compact = FALSE
){
  
  ## Exclude Individual Repo
  exclude_repo <- if (is.null(exclude_repo)) {
    ""
  } else {
    if (!is.character(exclude_repo)) stop("`exclude_repo` must be a character indicate repo names to exclude.", call. = FALSE)
    paste0("&exclude_repo=", paste(exclude_repo, collapse = ","))
  }
  
  ## Hide Individual Language
  hide <- if (is.null(hide)) {
    ""
  } else {
    if (!is.character(hide)) stop("`hide` must be a character indicate which language(s) to hide.")
    paste0("&hide=", paste(hide, collapse = ","))
  }
  
  ## Language Count
  valid_langs_count <- (length(langs_count) == 1) && (langs_count %in% 1:10)
  if(!valid_langs_count) stop("`langs_count` must be one of 1 to 10.")
  
  langs_count <- paste0("&langs_count=", langs_count)
  
  ## Compact Language Card Layout
  layout_compact <- if(layout_compact){
    "&layout=compact"
  } else {
    ""
  }
  
  # Build URL
  glue::glue("[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username={username}{exclude_repo}{hide}{langs_count}{layout_compact})](https://github.com/{username}/github-readme-stats)
")
  
}