# Publisher payloads

These base64-encoded gzip payloads were extracted unchanged from the notes
publisher workflow. Keeping them outside the workflow keeps each GitHub Actions
`run` script within GitHub's 21,000-character limit. Both publisher workflows
read these files after checkout; they contain lesson sources, not credentials.
