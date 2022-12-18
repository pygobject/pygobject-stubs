{{ range .Versions }}
# {{ .Tag.Name }} ({{ datetime "02 Jan 2006" .Tag.Date }})

{{ range .CommitGroups -}}
{{ if .Title }}  ## {{ .Title }}{{end}}

{{ range .Commits -}}
{{ if .Subject }}* {{ .Subject }}{{end}}{{if .Refs}} ({{range .Refs}}#{{.Ref}}{{end}}){{end}}
{{ end }}
{{ end -}}

{{- if .NoteGroups -}}
{{ range .NoteGroups -}}
{{ .Title }}
{{ range .Notes }}
{{ .Body }}
{{ end }}
{{ end -}}
{{ end -}}

{{break}}

{{ end -}}
