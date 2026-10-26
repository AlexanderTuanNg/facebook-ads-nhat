-- Mọi timestamp: giờ Việt Nam, dạng 'YYYY-MM-DD HH:MM:SS'
CREATE TABLE IF NOT EXISTS accounts (
    id           INTEGER PRIMARY KEY,
    key          TEXT UNIQUE NOT NULL,          -- page_chinh, nick_chinh, nick_phu_1 ...
    type         TEXT NOT NULL CHECK (type IN ('page','profile')),
    arm          TEXT CHECK (arm IN ('A','B') OR arm IS NULL),
    fb_id        TEXT,
    status       TEXT NOT NULL DEFAULT 'active', -- active | paused | restricted
    notes        TEXT
);

CREATE TABLE IF NOT EXISTS groups (
    id             INTEGER PRIMARY KEY,
    url            TEXT UNIQUE NOT NULL,
    name           TEXT,
    members        INTEGER,
    topic          TEXT,
    rules          TEXT,
    quality_score  REAL,
    status         TEXT NOT NULL DEFAULT 'candidate', -- candidate | requested | joined | left | banned | cho_tra_loi (nhóm hỏi câu khi vào, chưa trả lời — tools/vao_nhom.py) | bo_qua (mình bỏ qua: sai vùng — tools/vao_nhom.py)
    joined_at      TEXT,
    warmup_until   TEXT,
    arm            TEXT CHECK (arm IN ('A','B') OR arm IS NULL),
    account_id     INTEGER REFERENCES accounts(id),
    removed_count  INTEGER NOT NULL DEFAULT 0,
    notes          TEXT
);

CREATE TABLE IF NOT EXISTS posts (
    id              INTEGER PRIMARY KEY,
    slug            TEXT UNIQUE,
    pillar          TEXT,
    persona         TEXT,
    channel         TEXT NOT NULL CHECK (channel IN ('page','group')),
    target_id       INTEGER,           -- page: accounts.id | group: groups.id
    account_id      INTEGER REFERENCES accounts(id),
    arm             TEXT,              -- A | B | NULL (page)
    angle           TEXT,
    hook_type       TEXT,
    cta_type        TEXT,
    content_path    TEXT,
    status          TEXT NOT NULL DEFAULT 'planned',
    -- planned → review → approved|rejected → approved_human → scheduled|published|pending_approval|skipped|failed → removed
    compliance_note TEXT,
    scheduled_at    TEXT,
    published_at    TEXT,
    fb_post_id      TEXT,
    url             TEXT,
    created_at      TEXT NOT NULL DEFAULT (datetime('now','+7 hours')),
    updated_at      TEXT
);

CREATE TABLE IF NOT EXISTS metrics (
    id          INTEGER PRIMARY KEY,
    post_id     INTEGER NOT NULL REFERENCES posts(id),
    captured_at TEXT NOT NULL,
    reactions   INTEGER,
    comments    INTEGER,
    shares      INTEGER,
    views       INTEGER,
    alive       INTEGER,   -- 1 còn hiển thị, 0 bị xoá, NULL không rõ
    state       TEXT,      -- published | pending | removed
    source      TEXT       -- graph | browser
);

CREATE TABLE IF NOT EXISTS leads (
    id              INTEGER PRIMARY KEY,
    source_post_id  INTEGER REFERENCES posts(id),
    name            TEXT,
    channel_user    TEXT,   -- id/tên FB người comment
    contact         TEXT,
    need            TEXT,
    area            TEXT,
    budget          TEXT,
    stage           TEXT NOT NULL DEFAULT 'new', -- new | contacted | qualified | viewing | won | lost
    notes           TEXT,
    created_at      TEXT NOT NULL DEFAULT (datetime('now','+7 hours'))
);

CREATE TABLE IF NOT EXISTS account_health (
    id          INTEGER PRIMARY KEY,
    account_id  INTEGER NOT NULL REFERENCES accounts(id),
    at          TEXT NOT NULL,
    event       TEXT NOT NULL, -- ok | warning | checkpoint | restricted | blocked | session_expired | post_removed
    notes       TEXT
);

CREATE TABLE IF NOT EXISTS comments_handled (
    comment_id  TEXT PRIMARY KEY,
    fb_post_id  TEXT,
    action      TEXT,  -- replied | skipped | escalated
    handled_at  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS runs (
    id          INTEGER PRIMARY KEY,
    agent       TEXT,
    task        TEXT,
    started_at  TEXT,
    finished_at TEXT,
    summary     TEXT
);

-- Hợp đồng công việc (vòng trong): mỗi task có owner, tiêu chí nghiệm thu, loại bằng chứng bắt buộc.
-- Owner nộp bằng chứng → người kiểm chứng KHÁC owner ra phán quyết → Lead đóng task.
CREATE TABLE IF NOT EXISTS tasks (
    id                 INTEGER PRIMARY KEY,
    loop               TEXT NOT NULL DEFAULT 'inner',  -- outer | inner
    title              TEXT NOT NULL,
    owner              TEXT NOT NULL,                  -- tên agent
    inputs             TEXT,                           -- file/post id đầu vào còn hiệu lực
    acceptance         TEXT NOT NULL,                  -- tiêu chí nghiệm thu (gạch đầu dòng)
    evidence_required  TEXT NOT NULL,                  -- loại bằng chứng bắt buộc
    status             TEXT NOT NULL DEFAULT 'open',   -- open | submitted | verified | rejected | done | dropped
    evidence           TEXT,
    verifier           TEXT,
    verdict            TEXT,                           -- pass | fail
    verdict_note       TEXT,
    attempts           INTEGER NOT NULL DEFAULT 0,
    created_at         TEXT NOT NULL DEFAULT (datetime('now','+7 hours')),
    updated_at         TEXT
);

CREATE TABLE IF NOT EXISTS playbook_changes (
    id        INTEGER PRIMARY KEY,
    at        TEXT NOT NULL DEFAULT (datetime('now','+7 hours')),
    change    TEXT NOT NULL,
    reason    TEXT,
    evidence  TEXT
);

-- Số quảng cáo trả tiền theo tuần (tools/doc_ads.py --luu; skill quang-cao-bds)
CREATE TABLE IF NOT EXISTS ad_metrics (
    id            INTEGER PRIMARY KEY,
    ma_qc         TEXT NOT NULL,      -- mã mẫu QC trong tên quảng cáo, vd QC-A1
    y_tuong       TEXT,               -- mã ý tưởng, vd QC-A (workspace/plans/kho-y-tuong-qc.md)
    tu_ngay       TEXT,               -- YYYY-MM-DD đầu kỳ báo cáo
    den_ngay      TEXT,               -- YYYY-MM-DD cuối kỳ báo cáo
    chi_tieu      REAL,               -- VND
    hien_thi      INTEGER,
    tiep_can      INTEGER,
    tan_suat      REAL,
    luot_bam      INTEGER,
    lead          INTEGER,
    nghe_may      INTEGER,            -- NULL = file lead không có cột nghe_may
    du_chat_luong INTEGER,            -- Qualified + Converted
    xem_dat       INTEGER,            -- Converted
    coc           INTEGER,
    quyet_dinh    TEXT,               -- đề xuất TẮT/GIỮ/TĂNG lúc lưu
    captured_at   TEXT NOT NULL DEFAULT (datetime('now','+7 hours')),
    UNIQUE (ma_qc, tu_ngay, den_ngay)
);

INSERT OR IGNORE INTO accounts(key, type, arm, notes) VALUES
    ('page_chinh', 'page',    NULL, 'Fanpage chính: Graph API'),
    ('nick_chinh', 'profile', 'A',  'Nick chính: bán tự động'),
    ('nick_phu_1', 'profile', 'B',  'Nick phụ: tự động');
