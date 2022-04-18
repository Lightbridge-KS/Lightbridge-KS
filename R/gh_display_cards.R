#' Display Github Cards Side by Side
#'
#' @param username Your Github username
#' @param src_lt URL of Left Github card
#' @param src_rt URL of Right Github card
#' @param height Height of the cards
#'
#' @return `shiny.tag` object
#' @export
#'
gh_display_cards <- function(username, 
                             src_lt, 
                             src_rt, 
                             height = "160em"
) {
  
  htmltools::withTags(
    p(
      align = "center",
      a(
        href = paste0("https://github.com/", username),
        img(height = height, src = src_lt),
        img(height = height, src = src_rt)
      )
    )
  )
  
}