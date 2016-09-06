(defproject layton_trashmoving "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :plugins [[cider/cider-nrepl "0.10.0-SNAPSHOT"]]
  :main layton-trashmoving.core
  :dependencies [
                 [org.clojure/clojure "1.7.0"]
                 [org.clojure/tools.nrepl "0.2.10"]
                 [clj-http "2.0.0" ]
                 [org.clojure/data.json "0.2.6"]
                 [org.clojure/math.combinatorics "0.1.1"]
                 ])
