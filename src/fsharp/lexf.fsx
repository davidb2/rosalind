let rec f xs acc n = seq {
  match n with
  | 0 -> yield acc
  | _ -> seq { for x in xs -> yield f xs (x::acc) (n-1) }
}


