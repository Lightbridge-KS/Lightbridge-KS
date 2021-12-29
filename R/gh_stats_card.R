

# Stats Card --------------------------------------------------------------

#' Create GitHub Stats Card 
#'
#' @param username Your Github username
#' @param hide If not `NULL`, provide stats to hide, one of: stars, commits, prs, issues, contribs.
#' @param count_private (Boolean) `TRUE` to add the count of all your private contributions to the total commits count
#' @param show_icons (Boolean) `TRUE` to enable icons
#' @param theme If not `NULL`, provide build in theme names, e.g., one of: dark, radical, merko, gruvbox, tokyonight, onedark, cobalt, synthwave, highcontrast, dracula.
#'
#' @return A character rendering GitHub Stats Card to be inserted into R Markdown "github_document"
#' @export
#' @source https://github.com/anuraghazra/github-readme-stats
#' 
gh_stats_card <- function(username,
                          hide = NULL,
                          count_private = FALSE,
                          show_icons = FALSE,
                          theme = NULL
){
  
  url <- gh_stats_card_url(username = username, 
                           hide = hide, 
                           count_private = count_private, 
                           show_icons = show_icons, 
                           theme = theme)
  
  ### Build Markdown Link
  glue::glue("[![{username} GitHub stats]({url})](https://github.com/{username}/{username})")
  
}


# Github Stats Card URL ---------------------------------------------------



#' Create GitHub Stats Card URL 
#'
#' @param username Your Github username
#' @param hide If not `NULL`, provide stats to hide, one of: stars, commits, prs, issues, contribs.
#' @param count_private (Boolean) `TRUE` to add the count of all your private contributions to the total commits count
#' @param show_icons (Boolean) `TRUE` to enable icons
#' @param theme If not `NULL`, provide build in theme names, e.g., one of: dark, radical, merko, gruvbox, tokyonight, onedark, cobalt, synthwave, highcontrast, dracula.
#'
#' @return A URL of GitHub Stats Card
#' @export
#' @source https://github.com/anuraghazra/github-readme-stats
#' 
gh_stats_card_url <- function(username,
                              hide = NULL,
                              count_private = FALSE,
                              show_icons = FALSE,
                              theme = NULL
) {
  
  ## Hide Individual Stats
  hide <- if (is.null(hide)) {
    ""
  } else {
    ## Options: Stats to Hide
    stats_nm <- match.arg(hide,
                          choices = c("stars", "commits", "prs", "issues", "contribs")
    )
    paste0("&hide=", paste(stats_nm, collapse = ","))
  }
  
  ## Count Private
  count_private <- if (count_private) {
    "&count_private=true"
  } else {
    ""
  }
  
  ## Show Icons
  show_icons <- if (show_icons) {
    "&show_icons=true"
  } else {
    ""
  }
  ## Theme
  theme <- if (is.null(theme)) {
    ""
  } else {
    paste0("&theme=", theme)
  }
  
  ### Build Markdown Link
  glue::glue("https://github-readme-stats.vercel.app/api?username={username}{hide}{count_private}{show_icons}{theme}")
}

